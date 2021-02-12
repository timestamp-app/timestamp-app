import { AzureFunction, Context, HttpRequest } from "@azure/functions"
import { add_key_values, format_datetime } from "./wrangler"

const httpTrigger: AzureFunction = async function (context: Context, req: HttpRequest): Promise<void> {
    context.log('Input Triggered');
    add_key_values(req.body);
    format_datetime(req.body);

    context.res = {
        body: req.body
    };

};

export default httpTrigger;
