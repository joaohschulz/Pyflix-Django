/* Interações locais do catálogo; os endpoints e formulários do Django são preservados. */
(() => {
  const search = document.querySelector('#campo-busca');
  const form = document.querySelector('#catalogo-busca');
  const status = document.querySelector('#resultado-busca');
  const normalize = (value) => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase('pt-BR');
  function filterCatalog() {
    const query = normalize(search.value.trim());
    let count = 0;
    document.querySelectorAll('.card').forEach((card) => {
      const matches = normalize(`${card.dataset.title} ${card.dataset.category}`).includes(query);
      card.hidden = !matches;
      if (matches) count++;
    });
    document.querySelectorAll('.fileira').forEach((section) => {
      section.hidden = Boolean(query) && !section.querySelector('.card:not([hidden])');
    });
    if (status) {
      status.hidden = !query;
      status.textContent = count ? `${count} título${count === 1 ? '' : 's'} encontrado${count === 1 ? '' : 's'} no catálogo.` : 'Nenhum título encontrado. Tente outro nome ou categoria.';
    }
  }
  search?.addEventListener('input', filterCatalog);
  form?.addEventListener('submit', (event) => {
    event.preventDefault();
    filterCatalog();
    document.querySelector('#catalogo')?.scrollIntoView({ block: 'start' });
  });

  const container = document.querySelector('#modal-container');
  let previousFocus;
  let currentOverlay;
  function closeModal() {
    container?.replaceChildren();
  }
  function syncModal() {
    const overlay = container?.querySelector('.modal-overlay');
    document.body.classList.toggle('modal-aberto', Boolean(overlay));
    if (overlay && overlay !== currentOverlay) {
      previousFocus = document.activeElement;
      overlay.querySelector('.modal-fechar')?.focus();
    } else if (!overlay && currentOverlay) {
      if (previousFocus?.isConnected) previousFocus.focus();
    }
    currentOverlay = overlay;
  }
  container?.addEventListener('click', (event) => {
    if (event.target.matches('.modal-overlay') || event.target.closest('[data-modal-close]')) closeModal();
  });
  document.addEventListener('keydown', (event) => {
    if (!currentOverlay) return;
    if (event.key === 'Escape') closeModal();
    if (event.key !== 'Tab') return;
    const targets = [...currentOverlay.querySelectorAll('button, a[href], input, select, textarea, summary, [tabindex="0"]')].filter((el) => !el.disabled && el.getClientRects().length);
    const first = targets[0];
    const last = targets[targets.length - 1];
    if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last?.focus(); }
    else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first?.focus(); }
  });
  if (container) new MutationObserver(syncModal).observe(container, { childList: true, subtree: true });
})();
