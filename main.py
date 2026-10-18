import os 
import sys 
from networksecurity.logging import logger 
from networksecurity.exception.exception import NetworkSecurityException


def test_exception(): 
    try: 
        logger.logging.info("Zero division error") 
        a =1/0 
    except Exception as e: 
        raise NetworkSecurityException(e,sys)


if __name__=="__main__": 
    try: 
        test_exception()

    except Exception as e: 
        print(e)    