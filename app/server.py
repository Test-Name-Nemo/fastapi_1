import crud
import models
import schema
from depenedency import SessionDependency
from fastapi import FastAPI
from lifespan import lifespan


app = FastAPI(title="ADV", version="0.1",
              description="FDxsh", lifespan=lifespan)


@app.get("/v1/advertisement/{query_string}", response_model=list[
    schema.GetAdvResponse])
async def get_adv_by_author(session: SessionDependency, author: str):
    total = await crud.get_author(session, models.Adv, author)
    return [i[0].dict for i in total]


@app.post('/v1/advertisement/', response_model=schema.CreateAdvResponse,
          summary="Create new advertisement item")
async def create_advertisement(adv_json: schema.CreateAdvRequest,
                               session: SessionDependency):
    adv = models.Adv(**adv_json.model_dump())
    adv = await crud.add_item(session, adv)
    return {'id': adv.id}


@app.get("/v1/advertisement/{adv_id}", response_model=schema.
         GetAdvResponse)
async def get_adv(session: SessionDependency, adv_id: int):
    adv = await crud.get_item_id(session, models.Adv, adv_id)
    return adv.dict


@app.patch('/v1/advertisement/{adv_id}/', response_model=schema.
           UpdateAdvResponse)
async def update_advertisement(adv_json: schema.UpdateAdvRequest,
                               session: SessionDependency, adv_id: int):
    adv = await crud.get_item_id(session, models.Adv, adv_id)
    adv_dict = adv_json.model_dump(exclude_unset=True)
    for field, value in adv_dict.items():
        setattr(adv, field, value)
    adv = await crud.add_item(session, adv)
    return adv.dict


@app.delete("/v1/advertisement/{advertisement_id}",
            response_model=schema.DeleteAdvResponse)
async def delete_adv(todo_id: int, session: SessionDependency):
    await crud.delete_item(session, models.Adv, todo_id)
    return {"status": "Ok"}
