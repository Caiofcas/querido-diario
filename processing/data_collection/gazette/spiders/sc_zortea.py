from gazette.spiders.base import FecamGazetteSpider


class ScZorteaSpider(FecamGazetteSpider):
    name = "sc_zortea"
    FECAM_QUERY = "cod_entidade:296"
    TERRITORY_ID = "4219853"
