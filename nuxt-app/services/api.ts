export const useApi = () => {
  const config = useRuntimeConfig();

  const get = async (endpoint: string, options = {}) => {
    return await $fetch(endpoint, {
      baseURL: config.public.apiBase,
      method: 'GET',
      ...options,
      onResponseError({ response }) {
        console.error('Backend Error:', response._data);
      }
    });
  };

  return { get };
};