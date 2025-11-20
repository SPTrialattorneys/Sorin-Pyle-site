document.addEventListener('DOMContentLoaded', function() {

    // --- HOMEPAGE LOGO LINK BEHAVIOR ---
    // Prevent page reload when clicking logo on homepage
    const logoLink = document.querySelector('.navbar_logo-link');
    if (logoLink) {
        const currentPath = window.location.pathname;
        const isHomepage = currentPath === '/' || currentPath.endsWith('/index.html') || currentPath.endsWith('/');
        if (isHomepage) {
            logoLink.addEventListener('click', (e) => {
                e.preventDefault();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }
    }

    // --- DESKTOP DROPDOWN NAVIGATION ---
    const dropdownToggles = document.querySelectorAll('.navbar_dropdown-toggle');

    dropdownToggles.forEach(toggle => {
        const dropdown = toggle.closest('.navbar_dropdown');

        // Click handler for toggle
        toggle.addEventListener('click', (e) => {
            e.preventDefault();
            dropdown.classList.toggle('is-open');

            // Update ARIA attributes
            const isExpanded = dropdown.classList.contains('is-open');
            toggle.setAttribute('aria-expanded', isExpanded);
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', (e) => {
            if (!dropdown.contains(e.target)) {
                dropdown.classList.remove('is-open');
                toggle.setAttribute('aria-expanded', 'false');
            }
        });

        // Keyboard navigation support
        toggle.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                dropdown.classList.remove('is-open');
                toggle.setAttribute('aria-expanded', 'false');
                toggle.focus();
            }
        });
    });

    // --- MOBILE DROPDOWN NAVIGATION ---
    const mobileDropdownToggles = document.querySelectorAll('.mobile-nav_dropdown-toggle');

    mobileDropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', function() {
            const dropdown = this.closest('.mobile-nav_dropdown');
            const isOpen = dropdown.classList.contains('is-open');

            // Close all other mobile dropdowns
            document.querySelectorAll('.mobile-nav_dropdown').forEach(otherDropdown => {
                if (otherDropdown !== dropdown) {
                    otherDropdown.classList.remove('is-open');
                    const otherToggle = otherDropdown.querySelector('.mobile-nav_dropdown-toggle');
                    otherToggle.setAttribute('aria-expanded', 'false');
                }
            });

            // Toggle current dropdown
            dropdown.classList.toggle('is-open');
            this.setAttribute('aria-expanded', !isOpen);
        });
    });

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
                    isVisible = false;
                }
                return;
            }

            const scrollY = window.scrollY;
            const shouldShow = scrollY > showThreshold;

            if (shouldShow && !isVisible) {
                // Show the button using CSS transform+visibility (no CLS)
                mobileCTA.classList.add('is-visible');
                mobileCTA.setAttribute('aria-hidden', 'false');
                isVisible = true;
            } else if (!shouldShow && isVisible) {
                // Hide the button using CSS transform+visibility (no CLS)
                mobileCTA.classList.remove('is-visible');
                mobileCTA.setAttribute('aria-hidden', 'true');
                isVisible = false;
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
