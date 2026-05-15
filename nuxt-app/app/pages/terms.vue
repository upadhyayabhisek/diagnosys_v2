<template>
  <div class="min-h-screen bg-[var(--bg)] transition-colors duration-500">
    <div class="max-w-7xl mx-auto px-8 py-24 lg:py-32">
      <div class="flex flex-col lg:flex-row gap-20">
        <aside class="lg:w-1/3 lg:sticky lg:top-32 h-fit">
          <div class="space-y-6">
            <div
              class="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-red-500/10 text-red-500 text-[10px] font-bold uppercase tracking-widest border border-red-500/20"
            >
              Legal Framework
            </div>
            <h1
              class="text-5xl font-black tracking-tight text-[var(--text)] leading-[0.9]"
            >
              Terms of <br />
              Service.
            </h1>
            <div class="h-1 w-12 bg-red-500 rounded-full"></div>
            <div class="pt-4">
              <p
                class="text-[var(--subtext)] text-sm font-medium max-w-[280px] leading-relaxed"
              >
                Operating guidelines for the diagnosys research interface.
                Please read thoroughly.
              </p>
            </div>
          </div>
        </aside>

        <article
          class="lg:w-2/3 border-l border-[var(--border)] lg:pl-20 space-y-24"
        >
          <section class="max-w-2xl">
            <h2
              class="text-xs font-black uppercase tracking-[0.2em] text-red-500 mb-8"
            >
              Critical Notice
            </h2>
            <div
              class="bg-red-500/5 border border-red-500/10 p-8 rounded-2xl space-y-4"
            >
              <p class="text-[var(--text)] text-xl font-bold leading-tight">
                diagnosys is an experimental Machine Learning interface. It is
                not a licensed medical diagnostic tool.
              </p>
              <p class="text-[var(--subtext)] text-sm leading-relaxed">
                By interacting with our models, you acknowledge that outputs may
                be inaccurate or hallucinated. Usage is entirely at your own
                volition. Always consult a human medical professional for health
                concerns.
              </p>
            </div>
          </section>

          <section class="max-w-2xl">
            <h2
              class="text-xs font-black uppercase tracking-[0.2em] text-[var(--subtext)] mb-8"
            >
              01. Service Scope
            </h2>
            <div
              class="text-[var(--subtext)] text-lg leading-relaxed space-y-6"
            >
              <p>
                The platform is provided for
                <span class="text-[var(--text)] font-semibold text-base"
                  >Educational and Benchmarking purposes only</span
                >. It does not constitute a doctor-patient relationship.
              </p>
              <p>
                diagnosys grants you a limited, non-exclusive license to use the
                prediction models for personal learning. Commercial or clinical
                use is strictly prohibited.
              </p>
            </div>
          </section>

          <section class="max-w-2xl">
            <h2
              class="text-xs font-black uppercase tracking-[0.2em] text-[var(--subtext)] mb-8"
            >
              02. Liability Limitation
            </h2>
            <div class="text-[var(--subtext)] text-lg leading-relaxed">
              <p>
                diagnosys and its developers shall not be liable for any direct
                or indirect consequences arising from the interpretation of
                results. Accuracy is not guaranteed, and the platform is
                provided on an "as-is" basis.
              </p>
            </div>
          </section>

          <div
            class="pt-12 border-t border-[var(--border)] flex items-center justify-between"
          >
            <NuxtLink
              to="/"
              class="text-sm font-bold text-[var(--subtext)] hover:text-[var(--text)] transition-colors"
            >
              Decline
            </NuxtLink>
            <NuxtLink
              to="/signup"
              class="px-8 py-3 bg-[var(--subtext)] text-[var(--bg)] rounded-lg font-bold text-sm hover:opacity-90 transition-opacity"
            >
              Accept Terms
            </NuxtLink>
          </div>
        </article>
      </div>
    </div>
  </div>
</template>
