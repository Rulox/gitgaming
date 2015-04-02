from worker.celery_app import app
from developers.models import Developer
from django.core.exceptions import ObjectDoesNotExist
import logging
from traceback import format_exc
import traceback

logger = logging.getLogger("gitgaming_worker")


@app.task(name="worker.task.update_developer")
def update_developer(pk):
    """
        Update a given Developer and check if he has new badges.
        It also updates Developer's skills
    :param pk:
    :return:
    """
    try:
        developer = Developer.objects.get(pk=pk)
        developer.update_profile()
        developer.check_badges()
        developer.update_skills()
    except ObjectDoesNotExist:
        logger.error("[Developer Profile Update]: Developer con pk {pk} no existe".format(pk=pk))
        traceback.print_exc()
        return -1
    except:
        logger.error("Fallo actualizando developer con pk {pk}\n{ex_trace}".format(pk=pk, ex_trace=format_exc()))
        return -1
    return 0
