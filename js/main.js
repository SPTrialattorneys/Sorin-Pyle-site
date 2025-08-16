document.addEventListener('DOMContentLoaded', function() {

    // --- MOBILE NAVIGATION MENU ---
    const hamburgerButton = document.getElementById('hamburger-button');
    const mobileNav = document.getElementById('mobile-nav');

    if (hamburgerButton && mobileNav) {
        hamburgerButton.addEventListener('click', function() {
            // Toggle classes to show/hide menu and animate button
            mobileNav.classList.toggle('is-open');
            hamburgerButton.classList.toggle('is-active');

            // Lock body scroll when the mobile menu is open
            if (mobileNav.classList.contains('is-open')) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        });
    }

    // --- FAQ ACCORDION ---
    const faqItems = document.querySelectorAll('.faq_item');

    faqItems.forEach(item => {
        const question = item.querySelector('.faq_question');
        const answer = item.querySelector('.faq_answer');
        
        if(question && answer) {
            question.addEventListener('click', () => {
                const isOpen = item.classList.contains('is-open');

                // Close all other open FAQ items first for a cleaner accordion
                faqItems.forEach(otherItem => {
                    otherItem.classList.remove('is-open');
                    otherItem.querySelector('.faq_answer').style.maxHeight = 0;
                });

                // If the clicked item was not already open, open it
                if (!isOpen) {
                    item.classList.add('is-open');
                    answer.style.maxHeight = answer.scrollHeight + 'px';
                }
            });
        }
    });

    // --- FADE-UP ON SCROLL ANIMATION ---
    const elementsToAnimate = document.querySelectorAll('.fade-up-on-scroll');

    // Check if IntersectionObserver is supported
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1 // Trigger when 10% of the element is visible
        });

        elementsToAnimate.forEach(element => {
            observer.observe(element);
        });
    } else {
        // Fallback for older browsers: just show the elements
        elementsToAnimate.forEach(element => {
            element.classList.add('is-visible');
        });
    }

    // --- PRACTICE AREAS "SHOW MORE" BUTTON ---
    const showMoreBtn = document.getElementById('show-more-btn');
    const moreAreasContainer = document.getElementById('more-practice-areas');

    if (showMoreBtn && moreAreasContainer) {
        showMoreBtn.addEventListener('click', () => {
            moreAreasContainer.classList.toggle('is-expanded');

            if (moreAreasContainer.classList.contains('is-expanded')) {
                showMoreBtn.textContent = 'Show Less';
            } else {
                showMoreBtn.textContent = 'Show All Practice Areas';
            }
        });
    }

    // --- TABS FOR RESOURCES PAGE ---
    const tabButtons = document.querySelectorAll('.tab_button');
    const tabContents = document.querySelectorAll('.tab_content');

    if (tabButtons.length > 0 && tabContents.length > 0) {
        tabButtons.forEach(button => {
            button.addEventListener('click', () => {
                const targetId = button.getAttribute('data-tab');
                
                // Update buttons
                tabButtons.forEach(btn => btn.classList.remove('is-active'));
                button.classList.add('is-active');

                // Update content
                tabContents.forEach(content => {
                    if (content.id === targetId) {
                        content.classList.add('is-active');
                    } else {
                        content.classList.remove('is-active');
                    }
                });
            });
        });
    }
});
