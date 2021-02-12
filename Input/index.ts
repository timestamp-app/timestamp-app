import { AzureFunction, Context, HttpRequest } from "@azure/functions"
import { add_key_values, format_datetime } from "./wrangler"
import { Wirepusher } from "./wirepusher"

const httpTrigger: AzureFunction = async function (context: Context, req: HttpRequest): Promise<void> {
    context.log('Input Triggered');
    const wp = new Wirepusher(process.env.WIREPUSHER_ID);

    add_key_values(req.body);
    format_datetime(req.body);
    wp.notify("Success", "Record added")

    context.res = {
        body: req.body
    };

};

export default httpTrigger;
