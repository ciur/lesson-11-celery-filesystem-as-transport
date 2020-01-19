from django.shortcuts import render
from worker.tasks import ocr_document


def index(request):
    if request.method == 'POST':
        doc_name = request.POST.get('doc_name', False)
        ocr_document.apply_async(
            kwargs={'doc_name': doc_name},
        )
        context = {
            'message': f"Document {doc_name} submited for OCRing"
        }
        return render(request, 'app1/index.html', context)

    return render(request, 'app1/index.html', {})
