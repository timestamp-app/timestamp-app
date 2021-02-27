import { AzureFunction, Context, HttpRequest } from "@azure/functions"

const httpTrigger: AzureFunction = async function (context: Context, req: HttpRequest): Promise<void> {
    context.log('Output Triggered');
    const responseMessage = context.bindings.tableIn

    context.res = {
        body: responseMessage
    };

};

export default httpTrigger;
