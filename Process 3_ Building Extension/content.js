// content.js

let typingTimer;  // Biến để lưu timer
let doneTypingInterval = 1000;  // 1000ms = 1 giây trì hoãn

// Hàm gửi yêu cầu tới API và nhận dữ liệu phản hồi
async function convertToPolite(text) {
    try {
        console.log("Gửi yêu cầu tới API với dữ liệu:", text);
        const response = await fetch('http://127.0.0.1:8000/predict/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log("Dữ liệu nhận được từ API:", data);
        return data.polite;
    } catch (error) {
        console.error("Error calling API:", error);
        alert("Có lỗi xảy ra khi gọi API. Hãy kiểm tra console để biết thêm chi tiết.");
        return text;
    }
}

// Hàm xử lý khi người dùng nhập xong (với debounce)
async function handleInputEvent(target) {
    let originalText = target.value || target.innerText;

    // Nếu người dùng xóa hết nội dung, không gọi API
    if (!originalText.trim()) {
        console.log("⏳ Người dùng đã xóa hết nội dung. Chờ nhập lại...");
        return;
    }

    console.log("✏️ Phát hiện nhập liệu:", originalText);

    clearTimeout(typingTimer);
    typingTimer = setTimeout(async function () {
        let politeText = await convertToPolite(originalText);

        // Cập nhật văn bản ngay lập tức sau khi API trả về
        if (target.tagName === "INPUT" || target.tagName === "TEXTAREA") {
            target.value = politeText;
        } else if (target.isContentEditable) {
            target.innerHTML = politeText; // Dùng innerHTML để tránh Facebook reset
        }

        console.log("🔄 Chuyển đổi thành:", politeText);
    }, doneTypingInterval);
}

// Hàm gắn sự kiện input cho một phần tử
function attachInputListener(element) {
    if (
        element.tagName === "INPUT" ||
        element.tagName === "TEXTAREA" ||
        element.isContentEditable
    ) {
        element.addEventListener("input", function (event) {
            chrome.storage.sync.get("filterEnabled", function (data) {
                if (data.filterEnabled) {
                    handleInputEvent(event.target);
                }
            });
        });
        console.log("Đã gắn sự kiện cho phần tử:", element);
    }
}

// Gắn sự kiện cho các phần tử hiện có
document.querySelectorAll('INPUT, TEXTAREA, [contenteditable="true"]').forEach(attachInputListener);

// Sử dụng MutationObserver để theo dõi DOM thay đổi và gắn sự kiện cho phần tử mới
const observer = new MutationObserver((mutationsList) => {
    for (let mutation of mutationsList) {
        if (mutation.type === "childList" && mutation.addedNodes.length > 0) {
            mutation.addedNodes.forEach(node => {
                if (node.nodeType === Node.ELEMENT_NODE) {
                    attachInputListener(node);
                    node.querySelectorAll('input, textarea, [contenteditable="true"]').forEach(attachInputListener);
                }
            });
        }
    }
});

// Quan sát toàn bộ DOM để phát hiện các phần tử mới
observer.observe(document.body, { childList: true, subtree: true });