from django.http import JsonResponse

def response_error(code, reason):
    response = JsonResponse({
        "status": code,
        "message": reason
    })
    response.status_code = code
    return response

parameter_error = response_error(400, "invalid or insufficient parameters")
duplicate_error = response_error(400, "duplicate values in database")
