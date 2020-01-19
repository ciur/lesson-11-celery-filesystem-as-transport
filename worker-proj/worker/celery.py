from celery import Celery

app = Celery()

app.conf.update({
    'broker_url': 'filesystem://',
    'broker_transport_options': {
        'data_folder_in': '/lesson-11/broker/queue/',
        'processed_folder': '/lesson-11/broker/processed/',
        'store_processed': True
    },
    'include': 'worker.tasks',
})
