export const useAuth = () => {
  const user = useCookie("user_data", {
    watch: true,
    maxAge: 60 * 60 * 24 * 7,
    sameSite: "lax",
    path: "/",
  });

  const login = (userData) => {
    user.value = userData;
  };

  const logout = () => {
    user.value = null;
    navigateTo("/");
  };

  return {
    user,
    login,
    logout,
  };
};
