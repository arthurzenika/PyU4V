try:
    import ConfigParser as Config
except ImportError:
    import configparser as Config
import logging
import logging.config


def set_logger_and_config(logger):
    CFG = None
    # register configuration file
    try:
        CONF_FILE = 'PyU4V.conf'
        logging.config.fileConfig(CONF_FILE)
        CFG = Config.ConfigParser()
        CFG.read(CONF_FILE)
        LOG = logging.getLogger(logger.__name__)
    except Exception:
        # Set default logging handler to avoid "No handler found" warnings.
        try:  # Python 2.7+
            from logging import NullHandler
        except ImportError:
            class NullHandler(logging.Handler):
                def emit(self, record):
                    pass

        LOG = logging.getLogger(logger.__name__).addHandler(NullHandler())

    return LOG, CFG
