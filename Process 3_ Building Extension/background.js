// Khi extension được cài đặt hoặc cập nhật, thiết lập mặc định
chrome.runtime.onInstalled.addListener(() => {
    chrome.storage.sync.set({ filterEnabled: true }); // Mặc định tắt bộ lọc
    console.log("🛠 Extension đã cài đặt, bộ lọc mặc định TẮT.");
});

// Lắng nghe tin nhắn từ popup hoặc content script
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "toggleFilter") {
        chrome.storage.sync.set({ filterEnabled: message.state }, () => {
            console.log("🔄 Trạng thái bộ lọc cập nhật:", message.state);

            // Gửi thông báo đến tất cả content script đang chạy
            chrome.tabs.query({}, (tabs) => {
                tabs.forEach((tab) => {
                    chrome.scripting.executeScript({
                        target: { tabId: tab.id },
                        function: updateFilterStatus,
                        args: [message.state]
                    });
                });
            });
        });
    }
});

// Hàm cập nhật trạng thái bộ lọc trong content script
function updateFilterStatus(state) {
    chrome.storage.sync.set({ filterEnabled: state });
    console.log("🔔 Bộ lọc cập nhật trong content script:", state);
}
chrome.runtime.onStartup.addListener(() => {
    chrome.tabs.query({}, (tabs) => {
        tabs.forEach((tab) => {
            if (tab.id) {
                chrome.scripting.executeScript({
                    target: { tabId: tab.id },
                    files: ["content.js"]
                });
                console.log(`🔄 Inject content script vào tab ${tab.id}`);
            }
        });
    });
});
