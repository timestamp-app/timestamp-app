import { Record, add_key_values } from "./wrangler"

test("add keys", () => {
    let input: Record = {Lat: "44.4", Long: "66.6"};
    let expected: Record = { ...input };
    expected.PartitionKey = 1990;
    expected.RowKey = "12345j";

    expect(add_key_values(input)).toEqual(expected);
})
