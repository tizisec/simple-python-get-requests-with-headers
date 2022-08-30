import requests as req

		headers = {'Cookie': ''}
		resp = req.get(url="example.com",headers=headers)
			print("status code is: ",resp.status_code)
