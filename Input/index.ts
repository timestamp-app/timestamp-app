import { AzureFunction, Context, HttpRequest } from "@azure/functions"
import { add_key_values } from "./wrangler"

const httpTrigger: AzureFunction = async function (context: Context, req: HttpRequest): Promise<void> {
    context.log('Input Triggered');
    add_key_values(req.body);

    context.res = {
        body: req.body
    };

};

export default httpTrigger;
