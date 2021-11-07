from fastapi import APIRouter, HTTPException
from elasticsearch.exceptions import NotFoundError, ConnectionError
from typing import Optional
from app.connections import es, test_logger
import app.routers.envLog as envLog

router = APIRouter(
    tags=["search"]
)


@router.get("/search_cv")
def read_item(q: Optional[str] = None, contactInfoOnly: bool = False):
    srouceExcluseList = "info" if contactInfoOnly else ""

    try:
        test_logger.info('Search executed : ' + str(q))
        if q:
            logs = es.search(index="cv_search", query={
                             "match": {"info": q}}, _source_excludes=srouceExcluseList)
        else:
            logs = es.search(index="cv_search", query={
                             "match_all": {}}, _source_excludes=srouceExcluseList)
        return logs['hits']['hits']

    except NotFoundError:
        return []
    except ConnectionError:
        envLog.logFunction("error", 'Tried to reach "/search_cv", status : 500 - Internal Server Error (Cant reach ES instance)')
        raise HTTPException(status_code=500, detail="Internal Server Error")
