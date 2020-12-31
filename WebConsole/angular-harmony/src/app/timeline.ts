
export interface DataPoint {
    computer_name: string;
    cpu_percentage: number;
    memory_percentage: number;
    timestamp: string;
}

export interface Timeline {
    maxsize: number;
    timeline: DataPoint[];
}
