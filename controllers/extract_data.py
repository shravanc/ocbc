import glob
import logging
import os

from natsort import natsorted

from constant import PDF_UPLOAD_DIRECTORY, AWS_INSTANCE_IP, DEFAULT_PARSE_METHOD
from exceptions.exceptions_handler import *

from log import timeit






@timeit
def parse_document():
    return {"message": True}
