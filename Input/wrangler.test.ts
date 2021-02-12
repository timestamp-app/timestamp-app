import { Record, add_key_values } from "./wrangler";
import { v4 } from "uuid";

jest.mock("uuid");

beforeAll(() => {
    jest.useFakeTimers("modern");
    jest.setSystemTime(new Date(1990, 1, 1));
});

afterAll(() => {
    jest.useRealTimers();
});

test("add keys", () => {
    // Test Data
    const input: Record = {Lat: "44.4", Long: "66.6"};
    const expected: Record = { ...input };
    expected.PartitionKey = 1990;
    expected.RowKey = "12345j";

    // Mocks
    v4.mockReturnValue("12345j");

    // Run Function
    add_key_values(input)

    expect(input).toEqual(expected);
})
