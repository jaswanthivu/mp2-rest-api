import logging


def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    level = logging.INFO

    if verbose:
        level = logging.DEBUG

    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-8s %(name)s - %(message)s",
        datefmt="%H:%M:%S"
    )