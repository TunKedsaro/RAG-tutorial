def estimate_gemini_cost(response: object, input_cost_per_m:float=0.30, output_cost_per_m:float=2.50) -> dict:
    '''
    Estimate cost of a Gemini API response based on token usage.
    response : object
        The Gemini API response obj containing `usage_metadata` (inside response)
    input_cost_per_m  : float
        Input price $0.30 (text / image / video)
    output_cost_per_m : float
        Output price $2.50
    Return
    -------
    dict
        {
            "prompt_tokens": int,
            "output_tokens": int,
            "input_cost": float,
            "output_cost": float,
            "total_cost": float
        }
    '''
    tokens        = response.usage_metadata
    prompt_tokens = tokens.prompt_token_count
    output_tokens = tokens.candidates_token_count

    # Pricing
    # source : https://ai.google.dev/gemini-api/docs/pricing
    INPUT_COST_PER_M  = 0.30        # Gemini 2.5 Flash Input  tokens cost $0.30 per 1 million tokens
    OUTPUT_COST_PER_M = 2.50        # Gemini 2.5 Flash Output tokens cost $2.52 per 1 million tokens

    input_cost  = (prompt_tokens / 1000000) * INPUT_COST_PER_M
    output_cost = (output_tokens / 1000000) * OUTPUT_COST_PER_M
    total_cost  = input_cost + output_cost

    return {
            "prompt_tokens" : prompt_tokens,
            "output_tokens" : output_tokens,
            "input_cost"    : input_cost,
            "output_cost"   : output_cost,
            "total_cost"    : total_cost
        }