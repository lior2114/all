function getSiteKey(url) {
  try {
    const u = new URL(url);
    return u.origin;
  } catch (_) {
    return 'unknown';
  }
}

async function getActiveTab() {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  return tab;
}

async function init() {
  const tab = await getActiveTab();
  const siteKey = getSiteKey(tab.url || '');
  const enableEl = document.getElementById('enableSite');
  const delayEl = document.getElementById('delayStart');
  const reloadBtn = document.getElementById('reload');

  const stored = await chrome.storage.sync.get({ sites: {}, options: {} });
  const sites = stored.sites || {};
  const options = stored.options || {};

  enableEl.checked = sites[siteKey] !== false; // default enabled
  delayEl.checked = !!options.delayStart3s;

  enableEl.addEventListener('change', async () => {
    const newSites = { ...sites, [siteKey]: enableEl.checked };
    await chrome.storage.sync.set({ sites: newSites });
    // Notify content scripts to update
    chrome.tabs.sendMessage(tab.id, { type: 'QVD_SITE_ENABLE_CHANGED' });
  });

  delayEl.addEventListener('change', async () => {
    const newOptions = { ...options, delayStart3s: delayEl.checked };
    await chrome.storage.sync.set({ options: newOptions });
    chrome.tabs.sendMessage(tab.id, { type: 'QVD_OPTIONS_CHANGED' });
  });

  reloadBtn.addEventListener('click', () => chrome.tabs.reload(tab.id));
}

document.addEventListener('DOMContentLoaded', init);


