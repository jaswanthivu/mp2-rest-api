def test_upload_csv(client, sample_csv_bytes):
    response = client.post(
        "/upload",
        files={
            "file": (
                "sample_data.csv",
                sample_csv_bytes,
                "text/csv"
            )
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["rows"] == 6
    assert data["columns"] == 2
    assert isinstance(data["id"], int)
    assert data["id"] > 0


def test_process_and_retrieve(
    client, uploaded_dataset_id, processing_body
):
    process_response = client.post(
        f"/datasets/{uploaded_dataset_id}/process",
        json=processing_body
    )

    assert process_response.status_code == 200

    process_data = process_response.json()

    assert process_data["validation_rows_removed"] == 1
    assert process_data["cleaning_report"]["rows_before"] == 5
    assert process_data["cleaning_report"]["rows_after"] == 3

    retrieve_response = client.get(
        f"/datasets/{uploaded_dataset_id}"
    )

    assert retrieve_response.status_code == 200

    retrieved_data = retrieve_response.json()

    assert retrieved_data["total_rows"] == 3

    records = retrieved_data["data"]

    actual_records = {
        (record["student_id"], record["score"])
        for record in records
    }

    expected_records = {
        (1, 80),
        (2, 90),
        (5, 85)
    }

    assert actual_records == expected_records


def test_retrieve_missing_dataset(client):
    response = client.get("/datasets/999")

    assert response.status_code == 404