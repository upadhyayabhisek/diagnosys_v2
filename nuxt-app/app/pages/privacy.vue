<template>
  <div class="min-h-screen bg-[var(--bg)] transition-colors duration-500">
    <div class="max-w-7xl mx-auto px-8 py-24 lg:py-32">
      <div class="flex flex-col lg:flex-row gap-20">
        <aside class="lg:w-1/3 lg:sticky lg:top-32 h-fit">
          <div class="space-y-6">
            <div
              class="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-[var(--primary)]/10 text-[var(--primary)] text-[10px] font-bold uppercase tracking-widest border border-[var(--primary)]/20"
            >
              Data Privacy
            </div>
            <h1
              class="text-5xl font-black tracking-tight text-[var(--text)] leading-[0.9]"
            >
              Privacy <br />
              Policy.
            </h1>
            <div class="h-1 w-12 bg-[var(--primary)] rounded-full"></div>
            <div class="space-y-4 pt-4">
              <p
                class="text-[var(--subtext)] text-sm font-medium max-w-[280px] leading-relaxed"
              >
                Our commitment to protecting your data within the diagnosys
                research environment.
              </p>
              <div class="text-[11px] font-mono text-[var(--subtext)]/60">
                REVISION: 2026.03.23.A
              </div>
            </div>
          </div>
        </aside>

        <article
          class="lg:w-2/3 border-l border-[var(--border)] lg:pl-20 space-y-24"
        >
          <section class="max-w-2xl">
            <h2
              class="text-xs font-black uppercase tracking-[0.2em] text-[var(--subtext)] mb-8"
            >
              01. Information Collection
            </h2>
            <div
              class="space-y-6 text-[var(--text)] text-lg leading-relaxed font-medium"
            >
              <p>
                diagnosys operates as a
                <span
                  class="text-[var(--primary)] underline decoration-2 underline-offset-4"
                  >learning and research platform</span
                >. We prioritize data minimization, collecting only the inputs
                necessary to facilitate machine learning predictions.
              </p>
              <p class="text-[var(--subtext)]">
                This includes symptom descriptions, demographic age brackets,
                and general health metrics. No data is cross-referenced with
                external identity providers.
              </p>
            </div>
          </section>

          <section class="max-w-2xl">
            <h2
              class="text-xs font-black uppercase tracking-[0.2em] text-[var(--subtext)] mb-8"
            >
              02. Encryption Standards
            </h2>
            <div
              class="space-y-6 text-[var(--subtext)] text-lg leading-relaxed"
            >
              <p>
                All data in transit is protected via
                <span class="text-[var(--text)] font-bold"
                  >End-to-End Encryption (E2EE)</span
                >. However, because this is an educational simulation, we
                explicitly discourage the input of real-world Personally
                Identifiable Information (PII).
              </p>
              <blockquote
                class="border-l-2 border-[var(--primary)] pl-6 py-2 italic text-sm bg-[var(--card)] rounded-r-xl"
              >
                "Users remain anonymous by default. We do not store IP addresses
                or browser fingerprints in connection with health queries."
              </blockquote>
            </div>
          </section>

          <section class="max-w-2xl pb-20">
            <h2
              class="text-xs font-black uppercase tracking-[0.2em] text-[var(--subtext)] mb-8"
            >
              03. Model Training
            </h2>
            <div class="text-[var(--subtext)] text-lg leading-relaxed">
              <p>
                Aggregated, non-identifiable data is used to improve the
                weighting of our neural networks. This contributes to the global
                understanding of AI-driven medical assistance but never reveals
                individual user patterns.
              </p>
            </div>
          </section>

          <div class="pt-12 border-t border-[var(--border)]">
            <NuxtLink
              to="/"
              class="inline-flex items-center gap-2 text-sm font-bold text-[var(--primary)] hover:gap-4 transition-all"
            >
              <span>←</span> Back to Dashboard
            </NuxtLink>
          </div>
        </article>
      </div>
    </div>
  </div>
</template>
