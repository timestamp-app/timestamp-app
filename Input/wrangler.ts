import { v4 } from 'uuid';

interface Record {
    PartitionKey: number;
    RowKey: string;
    Lat: string;
    Long: string;
    DateTime: string;
}

function add_key_values(data: Record) {
    data.PartitionKey = new Date().getFullYear();
    data.RowKey = v4();
    return data;
}

export { add_key_values };
