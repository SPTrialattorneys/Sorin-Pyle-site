document.addEventListener('DOMContentLoaded', function() {

    // --- MOBILE NAVIGATION MENU ---
    const hamburgerButton = document.getElementById('hamburger-button');
    const mobileNav = document.getElementById('mobile-nav');

    if (hamburgerButton && mobileNav) {
        hamburgerButton.addEventListener('click', function() {
            const isExpanded = hamburgerButton.getAttribute('aria-expanded') === 'true';

            // Toggle ARIA attribute for accessibility
            hamburgerButton.setAttribute('aria-expanded', !isExpanded);

            // Toggle classes to show/hide menu and animate button
            mobileNav.classList.toggle('is-open');
            hamburgerButton.classList.toggle('is-active');

            // Update aria-hidden for screen readers
            mobileNav.setAttribute('aria-hidden', isExpanded ? 'true' : 'false');

            // Lock body scroll when the mobile menu is open
            if (mobileNav.classList.contains('is-open')) {
                // When menu is open
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
                    const otherQuestion = otherItem.querySelector('.faq_question');
                    const otherAnswer = otherItem.querySelector('.faq_answer');

                    otherItem.classList.remove('is-open');
                    otherAnswer.style.maxHeight = 0;

                    // Update ARIA attributes for closed items
                    otherQuestion.setAttribute('aria-expanded', 'false');
                    otherAnswer.setAttribute('aria-hidden', 'true');
                });

                // If the clicked item was not already open, open it
                if (!isOpen) {
                    item.classList.add('is-open');
                    answer.style.maxHeight = answer.scrollHeight + 'px';

                    // Update ARIA attributes for opened item
                    question.setAttribute('aria-expanded', 'true');
                    answer.setAttribute('aria-hidden', 'false');
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

    // --- MOBILE STICKY CTA BUTTON ---
    const mobileCTA = document.getElementById('mobile-cta-sticky');

    if (mobileCTA) {
        let isVisible = false;
        const showThreshold = 300; // Show after scrolling 300px past hero

        function isMobileDevice() {
            return window.innerWidth <= 768;
        }

        function handleScroll() {
            // Only run on mobile devices
            if (!isMobileDevice()) {
                // Ensure button is hidden on desktop
                if (isVisible) {
                    mobileCTA.classList.remove('is-visible');
                    mobileCTA.setAttribute('aria-hidden', 'true');
                    mobileCTA.style.display = 'none';
                    isVisible = false;
                }
                return;
            }

            const scrollY = window.scrollY;
            const shouldShow = scrollY > showThreshold;

            if (shouldShow && !isVisible) {
                // Show the button
                mobileCTA.style.display = 'block';
                mobileCTA.setAttribute('aria-hidden', 'false');
                // Trigger reflow to ensure display:block is applied before adding class
                mobileCTA.offsetHeight;
                mobileCTA.classList.add('is-visible');
                isVisible = true;
            } else if (!shouldShow && isVisible) {
                // Hide the button
                mobileCTA.classList.remove('is-visible');
                mobileCTA.setAttribute('aria-hidden', 'true');
                isVisible = false;
                // Hide completely after animation
                setTimeout(() => {
                    if (!isVisible) {
                        mobileCTA.style.display = 'none';
                    }
                }, 300);
            }
        }

        // Throttle scroll events for better performance
        let scrollTimeout;
        window.addEventListener('scroll', () => {
            if (scrollTimeout) {
                clearTimeout(scrollTimeout);
            }
            scrollTimeout = setTimeout(handleScroll, 10);
        });

        // Handle window resize to hide/show based on screen size
        window.addEventListener('resize', () => {
            handleScroll();
        });

        // Initial check
        handleScroll();
    }

});
