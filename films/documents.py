from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Film

@registry.register_document
class FilmDocument(Document):
    title = fields.TextField(fields={'keyword': fields.KeywordField()})
    original_language = fields.TextField(fields={'keyword': fields.KeywordField()})
    original_title = fields.TextField(fields={'keyword': fields.KeywordField()})
    overview = fields.TextField(fields={'keyword': fields.KeywordField()})
    poster_path = fields.TextField(fields={'keyword': fields.KeywordField()})
    
    class Index:
        name = 'films'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        # Modèle Django associé
        model = Film
        # Champs à indexer
        fields = [
            'popularity',
            'release_date',
            'vote_average',
            'vote_count',
        ]
