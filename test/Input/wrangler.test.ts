import { Record, add_key_values, format_datetime } from "../../Input/wrangler";
import { v4 } from "uuid";

jest.mock("uuid");

let input: Record;

beforeEach(() => {
    input = {DateTime: "January 20, 1990 at 08:55PM", Lat: "44.4", Long: "66.6"};
});

test("add keys", () => {
    const expected: Record = { ...input };
    expected.PartitionKey = 1990;
    expected.RowKey = "12345j";

    jest.useFakeTimers("modern");
    jest.setSystemTime(new Date(1990, 1, 1));
    v4.mockImplementationOnce(() => "12345j");

    add_key_values(input)

    expect(input).toEqual(expected);

    jest.useRealTimers();
});

test("format datetime", () => {
    const expected: Record = { ...input };
    expected.DateTime = "1990/01/20 20:55";

    format_datetime(input);

    expect(input).toEqual(expected);
});
