import { useRoute } from 'vue-router'

export function isActiveLink(routePath, exact = false) {
  const route = useRoute();
  if (exact) {
    return route.path === routePath;
  }
  return route.path.startsWith(routePath);
}
