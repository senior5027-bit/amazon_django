    document.addEventListener("DOMContentLoaded", () => {
        const images = document.querySelectorAll(".product-image");

        if (images.length === 0) {
            console.log("هیچ عکسی پیدا نشد.");
            return;
        }

        images.forEach((img, index) => {
            // اطمینان حاصل کنید که img.src به درستی آدرس تصویر را برمی‌گرداند
            // در حالت عادی، اگر img یک تگ <img> باشد، img.src همان URL تصویر است.
            // اگر img یک div با کلاس product-image باشد و تصویر داخل آن باشد، باید به تگ <img> دسترسی پیدا کنید.
            // بر اساس کد HTMLی که دادم، product-image روی div هست و img داخلشه.
            // پس باید اینجوری تغییرش بدیم:
            const imageElement = img.querySelector('img');
            if (imageElement) {
                console.log(`عکس ${index + 1}: ${imageElement.src}`);
                img.addEventListener("click", () => {
                    alert("آدرس عکس: " + imageElement.src);
                });
            } else {
                console.log(`عکس ${index + 1}: تگ <img> داخل product-image پیدا نشد.`);
            }
        });
    });
