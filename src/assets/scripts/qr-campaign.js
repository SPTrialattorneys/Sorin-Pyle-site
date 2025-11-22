/**
 * QR Campaign Page Interactions
 *
 * Handles interactive elements on go/*.html QR campaign landing pages:
 * - Accordion/toggle functionality
 * - Know Your Rights sections
 * - Resource expandable sections
 *
 * This file replaces inline onclick="toggleRight(this)" handlers for CSP compliance.
 */

document.addEventListener('DOMContentLoaded', function() {

    // Accordion Toggle Functionality
    // Uses class="toggle-accordion" on buttons/elements that should toggle parent active state
    document.querySelectorAll('.toggle-accordion').forEach(button => {
        button.addEventListener('click', function() {
            // Find the parent accordion item (either .accordion-item or direct parent)
            const parent = this.closest('.accordion-item') || this.parentElement;
            parent.classList.toggle('active');
        });
    });

    // Alternative: Direct click on accordion headers
    // Uses class="accordion-header" on clickable headers
    document.querySelectorAll('.accordion-header').forEach(header => {
        header.addEventListener('click', function() {
            const parent = this.closest('.accordion-item') || this.parentElement;
            parent.classList.toggle('active');
        });
    });

});
