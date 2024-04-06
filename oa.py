def parse_request(valid_auth_tokens, requests):
    responses = []
    
    for req in requests:
        if req[0] == "GET":
            auth_token = None
            parameters = {}
            for param in req[1].split('?')[-1].split('&'):
                key, value = param.split('=')
                if key == "token":
                    auth_token = value
                else:
                    parameters[key] = value

            if auth_token in valid_auth_tokens:
                response = "VALID" + "," + ",".join(parameters.keys()) + "," + ",".join(parameters.values())
            else:
                response = "INVALID"

            responses.append(response)

        elif req[0] == "POST":
            auth_token = None
            csrf_token = None
            parameters = {}
            for param in req[1].split('?')[-1].split('&'):
                key, value = param.split('=')
                if key == "token":
                    auth_token = value
                elif key == "csrf":
                    csrf_token = value
                else:
                    parameters[key] = value

            if auth_token in valid_auth_tokens and csrf_token is not None and csrf_token.isalnum() and len(csrf_token) >= 8:
                response = "VALID" + "," + ",".join(parameters.keys()) + "," + ",".join(parameters.values())
            else:
                response = "INVALID"

            responses.append(response)

    return responses

# Example inputs
valid_auth_tokens = ["ah37j2ha483u", "safh34ywb0p5", "ba34wyi8t902"]
requests = [["GET", "https://example.com/?token=347sd6yk8iu2&name=alex"],
            ["GET", "https://example.com/?token=safh34ywb0p5&name=sam"],
            ["POST", "https://example.com/?token=safh34ywb0p5&name=alex"],
            ["POST", "https://example.com/?token=safh34ywb0p5&csrf=ak2sh32dy&name=chris"]]

# Parsing requests
parsed_responses = parse_request(valid_auth_tokens, requests)
print(parsed_responses)  # Output: ["INVALID", "VALID,name,sam", "INVALID", "VALID,name,chris"]
