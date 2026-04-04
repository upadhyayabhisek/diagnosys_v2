
import { useApi } from './api';
export const useTestApi = () => {
    const { get } = useApi();

    const printOnBackend = async () => {
        try {
            return await get("/print");
        } catch (error) {
            return { error: "Failed to reach backend" };
        }
    };

    return { printOnBackend };
};