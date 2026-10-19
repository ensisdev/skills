// Brigadier starter (see 27). One builder per AST leaf; aliases forward to the canonical node.
package com.example.commands;

import com.mojang.brigadier.builder.LiteralArgumentBuilder;
import com.mojang.brigadier.arguments.StringArgumentType;

public final class ExampleBrigadier {

    // SourceT = your command source type (CommmandSourceStack or wrapper).
    public static LiteralArgumentBuilder<SourceT> root(ExampleService service) {
        return literal("example")
            .requires(src -> src.hasPermission("plugin.example.base"))
            .then(literal("create")
                .requires(src -> src.hasPermission("plugin.example.create"))
                .then(argument("name", StringArgumentType.word())
                    // suggestion provider: runtime registry, permission-filtered (11)
                    .suggests((ctx, builder) -> suggestNames(ctx.getSource(), builder))
                    .executes(ctx -> {
                        String name = StringArgumentType.getString(ctx, "name");
                        // usage vs domain errors per 08; locale keys per 48
                        service.create(ctx.getSource(), name);
                        return 1;
                    })))
            .then(literal("remove")
                .requires(src -> src.hasPermission("plugin.example.remove"))
                .then(argument("name", StringArgumentType.word())
                    .suggests((ctx, builder) -> suggestNames(ctx.getSource(), builder))
                    .executes(ctx -> {
                        // destructive leaf: confirmation flow first (23/34)
                        service.remove(ctx.getSource(), StringArgumentType.getString(ctx, "name"));
                        return 1;
                    })));
    }
}
