import { Record, add_key_values } from "./wrangler";

beforeAll(() => {
    jest.useFakeTimers("modern");
    jest.setSystemTime(new Date(1990, 1, 1));
});

afterAll(() => {
    jest.useRealTimers();
});

test("add keys", () => {
    const input: Record = {Lat: "44.4", Long: "66.6"};
    const expected: Record = { ...input };
    expected.PartitionKey = 1990;
    expected.RowKey = "12345j";

    expect(add_key_values(input)).toEqual(expected);
})
