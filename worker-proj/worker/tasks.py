import time
from celery import shared_task


@shared_task
def ocr_document(doc_name):
    # Pulling the document from shared storage
    # ...
    print("Hello!")
    time.sleep(15)
