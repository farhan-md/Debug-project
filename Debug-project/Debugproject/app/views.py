from django.shortcuts import render
from django.shortcuts import HttpResponse
import logging
# Create your views here.
logger = logging.getLogger(__name__)

def home_view(request):
    print("step 1 : home_view started")

    try:
        # Intentionally wrong field
        student = {"name" : "Ali", "age" : 20}
        logger.debug(f"student: {student}")
        # sending wrong variable to template
        return render(request, "app/home.html", {"student_name": student["namee"]})
    
    except Exception as e:
        logging.error(f"Error in home_view {e}")
        return HttpResponse("500 internal Server error",status=500)
    
def missing_view(request):
    # For 404 error
    return HttpResponse("This page exists but not mapped!")