import requests as req

		headers = {'Cookie': ''}
		resp = req.get(url="https://0a570041040060d3c0ae235b00e20027.web-security-academy.net/",headers=headers)
			print("status code is: ",resp.status_code)
