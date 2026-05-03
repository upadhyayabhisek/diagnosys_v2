export default defineNuxtRouteMiddleware((to) => {
    const user = useCookie<any>('user_data');

    const publicRoutes = ['/', '/login', '/signup'];

    if (!user.value) {
        if (to.path === '/admin' || to.path === '/dashboard') {
            return navigateTo('/login');
        }
        return;
    }

    const roleHome = user.value.role === 'admin' ? '/admin' : '/dashboard';

    if (publicRoutes.includes(to.path)) {
        return navigateTo(roleHome);
    }

    if (to.path === '/admin' && user.value.role !== 'admin') {
        return navigateTo('/dashboard');
    }

    if (to.path === '/dashboard' && user.value.role === 'admin') {
        return navigateTo('/admin');
    }
});