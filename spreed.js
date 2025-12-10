
const data = {
    to: 5,
    from: 1,
    [Symbol.iterator]: () => {
        let current = data.from;
        const last = data.to;
        return {
            next() {
                if (current <= last) {
                    return { done: false, value: current++ };
                } else {
                    return { done: true, value: undefined };
                }
            }
        };
    }
}

console.log(...data)