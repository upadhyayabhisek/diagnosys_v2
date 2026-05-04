<script setup lang="ts">
const props = defineProps<{ type: "login" | "signup" }>();
const router = useRouter();

const step = ref(1);
const loading = ref(false);
const errorMsg = ref("");
const form = ref({
  name: "",
  email: "",
  password: "",
  confirmPassword: "",
  birthday: "",
  gender: "",
});

const inputClass =
  "w-full p-3.5 bg-[var(--card)] border border-[var(--border)] rounded-2xl text-[var(--text)] focus:ring-2 focus:ring-[var(--primary)]/30 outline-none transition-all disabled:opacity-50";
const labelClass =
  "text-[10px] font-bold uppercase tracking-widest text-[var(--subtext)] ml-1 mb-1 block";

const validateForm = () => {
  errorMsg.value = "";

  if (!form.value.email.includes("@")) {
    errorMsg.value = "Please enter a valid email address.";
    return false;
  }
  if (form.value.password.length < 6) {
    errorMsg.value = "Password must be at least 6 characters.";
    return false;
  }

  if (props.type === "signup") {
    if (step.value === 1 && !form.value.name) {
      errorMsg.value = "Name is required.";
      return false;
    }
    if (
      step.value === 2 &&
      form.value.password !== form.value.confirmPassword
    ) {
      errorMsg.value = "Passwords do not match.";
      return false;
    }
  }
  return true;
};
const handleSubmit = async () => {
  if (!validateForm()) return;

  loading.value = true;
  const endpoint = props.type === "login" ? "/login" : "/register";
  try {
    const payload =
      props.type === "login"
        ? { email: form.value.email, password: form.value.password }
        : { ...form.value };
    const { login } = useAuth();
    const data: any = await $fetch(`http://localhost:5001${endpoint}`, {
      method: "POST",
      body: payload,
    });

    if (data.status === "success" && data.user) {
      login(data.user);

      if (data.user.role === "admin") {
        router.push("/admin");
      } else {
        router.push("/dashboard");
      }
    } else {
      errorMsg.value = data?.error || "Login failed.";
    }
  } catch (err: any) {
    const backendError = err.data?.error || err.data?.message;

    if (backendError === "account_disabled" || err.status === 403) {
      errorMsg.value =
        "Your account has been disabled. Please contact the administrator.";
    } else {
      errorMsg.value = backendError || "An error occurred. Please try again.";
    }
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div
    class="flex flex-col md:flex-row w-full min-h-[80vh] bg-[var(--background)] rounded-[2.5rem] overflow-hidden border border-[var(--border)] my-4"
  >
    <div
      class="hidden md:flex md:w-1/2 relative bg-[var(--primary)] items-center justify-center p-12"
    >
      <div class="absolute inset-0 z-0">
        <img
          src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80"
          class="w-full h-full object-cover opacity-30 mix-blend-overlay"
        />
      </div>
      <div class="relative z-10 text-white">
        <h1 class="text-5xl font-black tracking-tighter mb-4 leading-tight">
          Elevate Your <br />
          <span class="text-emerald-300">Wellbeing.</span>
        </h1>
        <p class="text-lg text-white/80 font-light max-w-sm">
          Join thousands tracking their health in one unified dashboard.
        </p>
      </div>
    </div>

    <div
      class="w-full md:w-1/2 flex items-center justify-center p-8 md:p-16 bg-[var(--card)]/30"
    >
      <div class="w-full max-w-sm">
        <div class="mb-8">
          <h2 class="text-3xl font-black text-[var(--text)] tracking-tight">
            {{ type === "login" ? "Welcome Back." : "Get Started." }}
          </h2>
          <p
            v-if="errorMsg"
            class="mt-2 text-xs font-bold text-red-500 uppercase tracking-widest"
          >
            {{ errorMsg }}
          </p>
        </div>

        <form class="space-y-5" @submit.prevent="handleSubmit">
          <template v-if="type === 'login'">
            <div class="space-y-4">
              <div>
                <label :class="labelClass">Email</label>
                <input
                  v-model="form.email"
                  type="email"
                  placeholder="name@example.com"
                  :class="inputClass"
                  required
                />
              </div>
              <div>
                <label :class="labelClass">Password</label>
                <input
                  v-model="form.password"
                  type="password"
                  placeholder="••••••••"
                  :class="inputClass"
                  required
                />
              </div>
            </div>
          </template>

          <template v-else>
            <div v-if="step === 1" class="space-y-4">
              <div>
                <label :class="labelClass">Full Name</label>
                <input
                  v-model="form.name"
                  type="text"
                  placeholder="John Doe"
                  :class="inputClass"
                />
              </div>
              <div class="grid grid-cols-2 gap-3">
                <div>
                  <label :class="labelClass">Birthday</label>
                  <input
                    v-model="form.birthday"
                    type="date"
                    :class="inputClass"
                  />
                </div>
                <div>
                  <label :class="labelClass">Gender</label>
                  <select v-model="form.gender" :class="inputClass">
                    <option value="" disabled>Select</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                  </select>
                </div>
              </div>
              <button
                type="button"
                @click="step = 2"
                class="w-full py-4 bg-[var(--text)] text-[var(--background)] font-bold rounded-2xl hover:opacity-90 transition-all"
              >
                Next Step
              </button>
            </div>

            <div v-if="step === 2" class="space-y-4">
              <div>
                <label :class="labelClass">Email Address</label>
                <input
                  v-model="form.email"
                  type="email"
                  placeholder="name@example.com"
                  :class="inputClass"
                />
              </div>
              <div class="grid grid-cols-2 gap-3">
                <input
                  v-model="form.password"
                  type="password"
                  placeholder="Password"
                  :class="inputClass"
                />
                <input
                  v-model="form.confirmPassword"
                  type="password"
                  placeholder="Confirm"
                  :class="inputClass"
                />
              </div>
              <button
                type="button"
                @click="step = 1"
                class="text-[10px] uppercase font-bold text-[var(--subtext)] hover:text-[var(--text)]"
              >
                ← Back to personal info
              </button>
            </div>
          </template>

          <!-- Submit Button -->
          <button
            v-if="type === 'login' || step === 2"
            type="submit"
            :disabled="loading"
            class="w-full py-4 bg-[var(--primary)] text-white font-bold rounded-2xl shadow-lg shadow-[var(--primary)]/20 hover:scale-[1.02] active:scale-[0.98] transition-all"
          >
            <span v-if="loading">Processing...</span>
            <span v-else>{{
              type === "login" ? "Sign In" : "Create Account"
            }}</span>
          </button>
        </form>

        <p class="mt-8 text-center text-xs font-medium text-[var(--subtext)]">
          <NuxtLink
            :to="type === 'login' ? '/signup' : '/login'"
            class="text-[var(--primary)] font-bold hover:underline"
          >
            {{
              type === "login"
                ? "Need an account? Sign Up"
                : "Have an account? Log In"
            }}
          </NuxtLink>
        </p>
      </div>
    </div>
  </div>
</template>
