export default defineNuxtRouteMiddleware((to) => {
    const user = useCookie<any>('user_data');
    const publicRoutes = ['/login', '/signup'];
    if (!user.value) {
        if (to.path.startsWith('/admin') || to.path.startsWith('/dashboard')) {
            return navigateTo('/login');
        }
        return;
    }
    const isAdmin = user.value.role === 'admin';
    const roleHome = isAdmin ? '/admin' : '/dashboard';
    if (publicRoutes.includes(to.path)) {
        return navigateTo(roleHome);
    }
    if (to.path.startsWith('/admin') && !isAdmin) {
        return navigateTo('/dashboard');
    }
    if (to.path.startsWith('/dashboard') && isAdmin) {
        return navigateTo('/admin');
    }
});