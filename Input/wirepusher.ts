import axios from "axios";

class Wirepusher {
    wirepusher_id: string;

    constructor(wirepusher_id: string) {
        this.wirepusher_id = wirepusher_id;
    }

    notify(status: string, message: string): void {
        const title = `Timestamp ${status}`;
        axios.post(`https://wirepusher.com/send?id=${this.wirepusher_id}&title=${title}&message=${message}&type=${status}`);
    }
}

export { Wirepusher };
