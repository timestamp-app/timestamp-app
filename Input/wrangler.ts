import { v4 } from 'uuid';
import * as moment from "moment"
import { Moment } from "moment"

interface Record {
    PartitionKey?: number;
    RowKey?: string;
    Lat?: string;
    Long?: string;
    DateTime?: string;
}

function add_key_values(data: Record): void {
    data.PartitionKey = new Date().getFullYear();
    data.RowKey = v4();
}

function format_datetime(data: Record): void {
    const inFmt = "MMMM DD, YYYY at hh:mmA";
    const outFmt = "YYYY/MM/DD HH:mm";
    const parsedDateTime: Moment = moment(data.DateTime, inFmt);
    data.DateTime = parsedDateTime.format(outFmt)
}

export { Record, add_key_values, format_datetime };
