// popup.js
document.addEventListener("DOMContentLoaded", function () {
    let toggleFilter = document.getElementById("toggleFilter");
    let statusText = document.getElementById("status");

    // Kiểm tra trạng thái lưu trước đó, nếu chưa có thì gán mặc định là false
    chrome.storage.sync.get("filterEnabled", function (data) {
        let filterEnabled = data.filterEnabled === undefined ? false : data.filterEnabled;
        toggleFilter.checked = filterEnabled;
        statusText.innerHTML = `Trạng thái: <b>${filterEnabled ? "Bật" : "Tắt"}</b>`;
    });

    // Lắng nghe sự kiện thay đổi của toggle filter
    toggleFilter.addEventListener("change", function () {
        let isEnabled = toggleFilter.checked;
        chrome.storage.sync.set({ "filterEnabled": isEnabled }, function () {
            statusText.innerHTML = `Trạng thái: <b>${isEnabled ? "Bật" : "Tắt"}</b>`;
        });
    });
});
