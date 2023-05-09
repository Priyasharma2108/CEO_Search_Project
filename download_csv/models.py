from django.db import models

# Create your models here.
class Name(models.Model):
    company_name = models.CharField(max_length=5000)


# if request.method == 'POST':
    #     company_name = request.POST.get('company_name')  # Assuming you're using a POST request and a form input field named 'company_name'
        
    #     openai.api_key = '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'

    #     # Set up the API endpoint
    #     endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"

    #     # Set up the request parameters
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": f"Bearer {openai.api_key}"
    #     }

    #     # Make a request to the OpenAI OAPI to retrieve company information
    #     # url = 'https://api.openai.com/v1/org-Cd3fCDiIbV3082BRADeGaown'  # Replace with the actual endpoint provided by OpenAI
    #     # headers = {
    #     #     'Authorization': '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',  # Replace with your actual OpenAI API key
    #     #     'Content-Type': 'application/json'
    #     # }

    #     data = {
    #         'company_name': company_name
    #     }
    #     response = requests.post(endpoint, headers=headers, json=data)

    #     if response.status_code == 200:
    #         company_data = response.json()
    #         founder = company_data.get('founder')
    #         director = company_data.get('director')
    #         print(company_data)
    #         return JsonResponse({'founder': founder,"director":director})
    #     else:
    #         return JsonResponse({'answer': 'No results found'})
    # return render(request,"index.html")