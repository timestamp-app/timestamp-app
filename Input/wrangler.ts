import { v4 } from 'uuid';

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


export { Record, add_key_values };
